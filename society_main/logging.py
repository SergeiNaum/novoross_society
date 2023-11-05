from polog import config, file_writer, field


def ip_extractor(log_item):
    request = log_item.function_input_data.args[0]
    ip = request.META.get('REMOTE_ADDR')
    return ip


def ip_converter(ip):
    """Делаем так, чтобы ip-адрес указывался через дефис."""
    return ip.replace('.', '-')


config.add_fields(ip=field(ip_extractor, converter=ip_converter))
config.add_fields(ip=field(ip_extractor))
config.add_handlers(file_writer('/home/sergeynaum/work_projects/novoross_society/logs/debug.json', rotation='200 megabytes >> archive', lock_type=None))
