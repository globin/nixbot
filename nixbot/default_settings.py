NIXBOT_BOT_NAME = 'nixborg'
NIXBOT_REPO = 'nixos/nixpkgs'
NIXBOT_PR_REPO = 'mayflower/nixpkgs-pr'
NIXBOT_PUBLIC_URL = 'https://bot.nixos.community'
NIXBOT_REPO_DIR = '/var/lib/nixbot/repositories'
NIXBOT_HYDRA_PROJECT = 'nixos'
NIXBOT_NIXEXPR_PATH = 'nixos/release-small.nix'
NIXBOT_GITHUB_TOKEN = '<insert github token>'
NIXBOT_GITHUB_SECRET = 'justnotsorandom'
NIXBOT_GITHUB_WRITE_COMMENTS = True
NIXBOT_CELERY_BROKER_URL = 'redis://localhost:6379'
NIXBOT_CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERYD_LOG_FORMAT = "[%(asctime)s: %(levelname)s/%(processName)s/%(name)s] %(message)s"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///var/lib/nixbot/db.sqlite'
