from shark.orm import Shark


class Makemigrations(Shark):

    def migrate(self):

        self.create_table(
            sql="""CREATE TABLE portfolio(
                        id INTEGER(21) AUTO_INCREMENT,
                        title CHAR(255) NOT NULL,
                        photo CHAR(150) NOT NULL,
                        PRIMARY KEY (id)
                    );""")
        self.installation_encoding(tablename="portfolio")

        self.create_table(
            sql="""CREATE TABLE works(
                        id INTEGER(21) AUTO_INCREMENT,
                        title CHAR(255) NOT NULL,
                        prices CHAR(50) NOT NULL,
                        photo CHAR(150) NOT NULL,
                        desk TEXT(1000) NOT NULL,
                        PRIMARY KEY (id)
                    );""")
        self.installation_encoding(tablename="works")

        self.create_table(
            sql="""CREATE TABLE comments(
                        id INTEGER(21) AUTO_INCREMENT,
                        photo CHAR(150) NOT NULL,
                        PRIMARY KEY (id)
                    );""")
        self.installation_encoding(tablename="comments")

        self.create_table(
            sql="""CREATE TABLE questions(
                        id INTEGER(21) AUTO_INCREMENT,
                        title CHAR(255) NOT NULL,
                        desk TEXT(1000) NOT NULL,
                        PRIMARY KEY (id)
                    );""")
        self.installation_encoding(tablename="questions")