from apscheduler.schedulers.background import BackgroundScheduler
from apps.weather.utils import WeatherController

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.print_jobs()


class JobController(WeatherController):

    def job_weather_create(self):
        try:
            scheduler.add_job(self.fetch_all, 'interval', minutes=1)
            scheduler.print_jobs()
        except Exception as e:
            print(f"Exception job_show_package_to_offer......{e.args}")

