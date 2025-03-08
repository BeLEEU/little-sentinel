import os

from config import Config
from scheduler import Scheduler
from github_client import GitHubClient
from notifier import Notifier
from report_generator import ReportGenerator
from subscription_manager import SubscriptionManager


def main():
    config = Config()
    github_api_key = os.getenv("GITHUB_API_KEY")
    github_client = GitHubClient(github_api_key)
    notifier = Notifier(config.notification_settings)
    report_generator = ReportGenerator()
    subscription_manager = SubscriptionManager(config.subscriptions_file)

    scheduler = Scheduler(
        github_client=github_client,
        notifier=notifier,
        report_generator=report_generator,
        subscription_manager=subscription_manager,
        interval=config.update_interval
    )

    scheduler.start()


if __name__ == "__main__":
    main()
