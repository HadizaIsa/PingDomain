from django_cron import CronJobBase, Schedule, logger
from .management.commands.ping_domains_periodically import check_domains


class PingDomainCronJob(CronJobBase):
    RUN_EVERY_MINS = 2
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'PING.ping_domain_cron_job'

    def do(self):
        check_domains()

