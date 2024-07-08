from apscheduler.schedulers.background import BackgroundScheduler

from src.application.services.message_orchestrator_service import MessageOrchestratorService

scheduler = BackgroundScheduler()
scheduler.add_job(MessageOrchestratorService.start, 'interval', seconds=5)
