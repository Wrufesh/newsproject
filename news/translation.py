from modeltranslation.translator import TranslationOptions, translator

from news.models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(News, NewsTranslationOptions)