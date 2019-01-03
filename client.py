#!/usr/bin/env python

import logging
import sys
import requests

from dns import rdatatype
from dnsknife import resolver

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def execute_query(domain):
    ans = resolver.query(domain, 'A')

    # Validating tht rrsig domain is in place
    rrsig_answer = False
    for answer in ans.response.answer:
        if answer.rdtype == rdatatype.RRSIG:
            rrsig_answer = True
            break
    if not rrsig_answer:
        logger.error("No RRSIG answer found in response")
        return False

    if len(ans) == 0:
        return False
    logger.info("Resolved '{0}' to '{1}'".format(domain, ans[0]))
    res = requests.get("http://{0}".format(ans[0]), timeout=5)
    if res.status_code != 200:
            return False
    return True


if __name__ == "__main__":
    try:
        res = execute_query(sys.argv[1])
        if res:
            sys.exit(0)
        sys.exit(1)
    except Exception as e:
        logger.error("Exception {0}".format(e))
        sys.exit(1)
