class Article:
    # dependent class!

    all = []


    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_to_validate):
        if isinstance(author_to_validate, Author):
            self._author = author_to_validate
        else:
            raise TypeError("Author must be of type Author")
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine_to_validate):
        if isinstance(magazine_to_validate, Magazine):
            self._magazine = magazine_to_validate
        else:
            raise TypeError("Magazine must be of type Magazine")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_to_validate):
        if not isinstance(title_to_validate, str):
            raise TypeError("Title must be a string")
        elif len(title_to_validate) < 5 or len(title_to_validate) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        else:
            self._title = title_to_validate



class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_to_validate):
        if not isinstance(name_to_validate, str):
            raise TypeError("Author name must be a string")
        elif len(name_to_validate) < 1:
            raise ValueError("Author name must be at least one")
        elif hasattr(self, "_name"):
            raise AttributeError("Author name cannot be reset!")
        else:
            self._name = name_to_validate

    def articles(self):
        #list comprehension
        return [article for article in Article.all if article._author is self]

    def magazines(self):
        #list() with a set for uniqueness
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        #new_article =
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        #list() with a set
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_to_validate):
        if not isinstance(name_to_validate, str):
            raise TypeError("Magazine name must be a string")
        elif len(name_to_validate) < 2 or len(name_to_validate) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters")
        else:
            self._name = name_to_validate

    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category_to_validate):
        if not isinstance(category_to_validate, str):
            raise TypeError("Magazine category must be a string")
        elif len(category_to_validate) < 1:
            raise ValueError("Magazine category must be at least one character")
        else:
            self._category = category_to_validate


    def articles(self):
        #list comprehension
        return [article for article in Article.all if article._magazine is self]


    def contributors(self):
        #list() with a set for uniqueness
        return list({article.author for article in self.articles()})


    def article_titles(self):
        # refer to articles()
        if not self.articles():
            return None
        return [article.title for article in self.articles()]


    def contributing_authors(self):
        # THIS ONE was tricky for me 
        # initialize an empty count set, and increment?
        # variable for contributing authors that meet criteria?
        author_counts = {}

        for article in self.articles():
            if article.author not in author_counts:
                author_counts[article.author] = 0  # Initialize count
            author_counts[article.author] += 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]

        return contributing_authors if contributing_authors else None
        

    

    #BONUS DELIVERABLE
    @classmethod
    #if not, return none
    #create a dictionary
    #update count for each article of that magazine
    #.get to retrieve from dictionary
    #return MAX (the MOST articles)
    def top_publisher():
        if not Article.all:
            return None
    
        magazine_counts = {}
    
    for article in Article.all:
        if article._magazine not in magazine_counts:
            magazine_counts[article._magazine] = 0
        magazine_counts[article._magazine] += 1

    return max(magazine_counts, key=magazine_counts.get) if magazine_counts else None