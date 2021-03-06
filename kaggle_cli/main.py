import sys
from cliff.app import App
from cliff.commandmanager import CommandManager


class KaggleCLI(App):

    def __init__(self):
        super(KaggleCLI, self).__init__(
            description='An unofficial Kaggle command line tool.',
            version='0.3',
            command_manager=CommandManager('kaggle_cli'),
        )


def main(argv=sys.argv[1:]):
    app = KaggleCLI()

    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
