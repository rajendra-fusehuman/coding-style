class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._config = cls._instance._read_config_file()
        return cls._instance

    def _read_config_file(self):
        config = {}
        with open("config.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return config

    def get_config(self, key):
        return self._config.get(key)


if __name__ == "__main__":
    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager()

    if config_manager1 == config_manager2:
        print("Both instances are the same!")

    print(config_manager1.get_config("server_ip"))
    print(config_manager2.get_config("port"))
    print(config_manager2.get_config("database_name"))
    print(config_manager2.get_config("username"))
