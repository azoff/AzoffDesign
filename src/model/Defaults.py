from ConfigParser import ConfigParser
from os import path

DEFAULTS = path.join(path.dirname(path.dirname(path.dirname(__file__))), "defaults.ini")

_parser = ConfigParser()

_parser.read(DEFAULTS)

class Defaults:

	BOT_EMAIL = _parser.get("defaults", "bot_email")
	TITLE = _parser.get("defaults", "title")
	DESCRIPTION = _parser.get("defaults", "description")
	KEYWORDS = _parser.get("defaults", "keywords")
	SCRIPTS = _parser.get("defaults", "scripts")
	STYLES = _parser.get("defaults", "styles")
	USE_MEMCACHE = _parser.getboolean("defaults", "memcache")
	COMPILE_MODE = _parser.get("defaults", "compile_mode")