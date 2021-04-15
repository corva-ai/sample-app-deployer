from corva import Api, Cache, Corva, ScheduledEvent


def lambda_handler(event, context):
    """
    This function is the main entry point of the AWS Lambda function
    :param event:
    :param context:
    :return:
    """
    corva = Corva(context=context)
    corva.scheduled(scheduled_app, event)


def scheduled_app(event: ScheduledEvent, api: Api, cache: Cache):
    print("Scheduled")
