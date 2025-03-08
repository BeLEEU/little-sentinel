class ReportGenerator:
    def generate(self, updates):
        # Implement report generation logic
        report = "最新发布的信息：\n\n"
        for repo, release in updates.items():
            report += f"仓库名称: {repo}\n"
            report += f"最新版本: {release['tag_name']}\n"
            report += f"发行名: {release['name']}\n"
            report += f"发行日期: {release['published_at']}\n"
            report += f"发行信息:\n{release['body']}\n"
            report += "-" * 40 + "\n"
        return report
