# coding=utf-8
from __future__ import absolute_import
import logging

import requests
from retrying import retry
from requests.exceptions import RequestException

from app.tasks import celery_app
from common import constants
from common.exception import RequestsError
from app.controllers.keyword import KeywordController
from app.controllers.jobs_count import JobsCountController
from app.utils.util import crawler_sleep
from app.utils.cookies import Cookies
from app.utils.http_tools import generate_http_header
from app.utils.time_tools import get_date_begin_by_timestamp
from app.controllers.job import get_jobs_statistics
from app.utils.cache import cache_clear


@celery_app.task()
def crawl_lagou_jobs_count():
    pre_date = get_date_begin_by_timestamp(after_days=-1)
    keywords = KeywordController.get_most_frequently_keywords(limit=2000)
    logging.info('{} crawl_lagou_job_count 定时任务运行中! 关键词 {} 个'.format(pre_date, len(keywords)))
    for keyword in keywords:
        city_jobs_count = {
            '全国': 0, '北京': 0, '上海': 0, '广州': 0, '深圳': 0, '杭州': 0, '成都': 0
        }
        for city in city_jobs_count:
            response_json = request_jobs_count_json(city=city, keyword=keyword)
            try:
                city_jobs_count[city] = response_json['content']['positionResult']['totalCount']
            except Exception:
                logging.getLogger(__name__).error('获取 jobs count 信息失败, 关键词为 {}'.format(keyword.name), exc_info=True)
        JobsCountController.add(date=pre_date, keyword_id=keyword.id,
                                all_city=city_jobs_count['全国'], beijing=city_jobs_count['北京'],
                                shanghai=city_jobs_count['上海'], guangzhou=city_jobs_count['广州'],
                                shenzhen=city_jobs_count['深圳'], hangzhou=city_jobs_count['杭州'],
                                chengdu=city_jobs_count['成都'])
    logging.info('crawl_lagou_job_count 任务完成!')
    # 失效缓存
    remove_count = cache_clear(get_jobs_statistics)
    logging.info('主动失效缓存成功, 数量{}'.format(remove_count))


@retry(stop_max_attempt_number=constants.RETRY_TIMES, stop_max_delay=constants.STOP_MAX_DELAY,
       wait_fixed=constants.WAIT_FIXED)
def request_jobs_count_json(city, keyword):
    query_string = {'needAddtionalResult': False}
    if city != '全国':
        query_string['city'] = city
    form_data = {
        'first': False,
        'pn': 1,
        'kd': keyword.name
    }
    headers = generate_http_header(is_crawl_jobs_count=True)
    crawler_sleep()
    try:
        cookies = Cookies.get_random_cookies()
        response = requests.post(url=constants.JOB_JSON_URL,
                                 params=query_string,
                                 data=form_data,
                                 headers=headers,
                                 cookies=cookies,
                                 allow_redirects=False,
                                 timeout=constants.TIMEOUT)
        response_json = response.json()
        if 'content' not in response_json:
            Cookies.remove_cookies(cookies)
            raise RequestsError(error_log='wrong response content')
    except RequestException as e:
        logging.error(e)
        raise RequestsError(error_log=e)
    return response_json
