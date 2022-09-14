import log_class.logger_factory_implement as logger_factory_implement_class


def main() -> None:
    type_logger = str(input("""
        [c]Para salida por consola
        [f]Para salida hacia el archivo
        [e]Para salida por email
        >>>: """))
    logger = logger_factory_implement_class.LoggerFactoryImplement().get_logger(type=type_logger)
    logger.print_info('Mensage generico', 200)
    logger.print_warning('Mensage generico', 404)
    logger.print_error('Mensage generico', 401)
    logger.print_debug('Mensage generico', 500)


if __name__ == '__main__':
    main()
