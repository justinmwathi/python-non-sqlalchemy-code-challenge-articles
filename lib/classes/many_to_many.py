class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if hasattr(self,"_title"):
            return (self.title)
        if not isinstance(title,str):
            raise TypeError("Title should be a string!")
        if len(title)>=5 or len(title)<=50:
            self._title=title


    @property
    def author(self):
        return self._author
    
    author.setter
    def author(self,author):
        if not isinstance(author,Author):
            return TypeError('author must be an instance of Author.')
        self._author=author
        

    @property
    def magazine(self):
        return self._magazine
    
    magazine.setter
    def magazine(self,magazine):
        if not isinstance(magazine,Magazine):
            return TypeError('magazine must be an instance of Magazine.')
        self._magazine=magazine 


class Author:
    all_authors=[]
    def __init__(self, name):

        if not isinstance(name, str) or len(name) == 0:

            raise ValueError("Author name must be a non-empty string")

        self._name = name
        Author.all_authors.append(self)

    @property

    def name(self):

        return self._name


    @name.setter

    def name(self, value):
        #if Author class has name attribute already instantiated
        if hasattr(self, '_name'):

            return (self.name)

        if not isinstance(value, str) or len(value) == 0:

            raise ValueError("Author name must be a non-empty string")

        self._name = value

        
    


    def articles(self):
        return [article for article in Article.all if article.author ==self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)

        self.articles().append(article)

        return article

    def topic_areas(self):
        if not self.articles():
            return None
        topic_areas=set()
        for article in self.articles():
            topic_areas.add(article.magazine.category)
        return list(topic_areas)

class Magazine:
    all=[]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all.append(self)
        
    @property
    def name(self):

        return self._name


    @name.setter

    def name(self, value):

        if not isinstance(value, str):

            raise ValueError("Name must be a string")

        if len(value) < 2 or len(value) > 16:

            raise ValueError("Name must be between 2 and 16 characters")

        self._name = value


    @property

    def category(self):

        return self._category


    @category.setter

    def category(self, value):

        if not isinstance(value, str):

            raise ValueError("Category must be a string")

        if len(value) <= 0:

            raise ValueError("Category must be longer than 0 characters")

        self._category = value
    def articles(self):
        return[article for article in Article.all if article.magazine==self]

    def contributors(self):
         return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        if not self.articles():
            return None
        titles=[article.title for article in self.articles()]
        return titles

    def contributing_authors(self):
        if not self.articles():

            return None

        authors_and_counts = {}

        for article in self.articles():

            if article.author in authors_and_counts:

                authors_and_counts[article.author] += 1

            else:

                authors_and_counts[article.author] = 1

        contributing_authors = [author for author, count in authors_and_counts.items() if count > 2]

        if not contributing_authors:

            return None

        return contributing_authors
    


  