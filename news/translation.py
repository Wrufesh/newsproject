from modeltranslation.translator import TranslationOptions, translator

from news.models import News, Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('headline', 'reporter', 'article')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)