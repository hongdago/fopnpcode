#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:dns_mx.py
DESC: 解析电子邮件域名
"""

import argparse, dns.resolver

def resolve_hostname(hostname, indent=''):
    "print an A or AAAA record for `hostname`; follow CNAMEs if necessary"
    indent = indent+'    '
    answer = dns.resolver.query(hostname, 'A')
    if answer.rrset is not None:
        for record in answer:
            print(indent, hostname, 'has A address', record.address)
        return
    answer = dns.resolver.query(hostname, 'AAAA')
    if answer.rrset is not None:
        for record in answer:
            print(indent, hostname, 'has AAAA address', record.address)
        return
    answer = dns.resolver.query(hostname, 'CNAME')
    if answer.rrset is not None:
        record = answer[0]
        cname = record.address
        print(indent, hostname, 'is a CNAME alias for', cname)
        resolve_hostname(cname, indent)
        return
    print(indent, 'ERROR: no A, AAAA, or CNAME record for', hostname)


def resolve_email_domain(domain):
    "For an email address `name@domain` find its mail server IP address"
    try:
        answer = dns.resolver.query(domain, 'MX', raise_on_no_answer=False)
    except dns.resolver.MXDOMAIN:
        print('Error: No Such domain', domain)
        return
    if answer.rrset is not None:
        records = sorted(answer, key=lambda record:record.preference)
        for record in records:
            name = record.exchange.to_text(omit_final_dot=True)
            print('Priority', record.preference)
            resolve_hostname(name)
    else:
        print('This domain has no explicit MX Records')
        print('Attempting to resolver it as an A, AAAA or CNAME')
        resolve_hostname(domain)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find mail server IP address')
    parser.add_argument('domain', help='domain that you want to send mail to')
    resolve_email_domain(parser.parse_args().domain)