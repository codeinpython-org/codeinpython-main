from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from task.models import Category, Post


class Command(BaseCommand):
    help = 'Populates the database with some testing data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Started database population process...'))

        if User.objects.filter(username="satyajit").exists():
            self.stdout.write(self.style.SUCCESS('Database has already been populated. Cancelling the operation.'))
            return

        # Create users
        satyajit = User.objects.create_user(username='satya', password='really_strong_password123')
        satyajit.first_name = 'Satyajit'
        satyajit.last_name = 'Barik'
        satyajit.save()

        jess = User.objects.create_user(username='jess_', password='really_strong_password123')
        jess.first_name = 'Jess'
        jess.last_name = 'Brown'
        jess.save()

        johnny = User.objects.create_user(username='johnny', password='really_strong_password123')
        johnny.first_name = 'Johnny'
        johnny.last_name = 'Davis'
        johnny.save()

        # Create categories
        system_administration = Category.objects.create(name='System administration')
        seo_optimization = Category.objects.create(name='SEO optimization')
        programming = Category.objects.create(name='Programming')

        # Create articles
        website_article = Post.objects.create(
           title='How to code and deploy a website?',
           created_by=satyajit,
           type='TU',
           content='There are numerous ways of how you can deploy a website...',
        )
        website_article.save()
        website_article.categories.add(programming, system_administration, seo_optimization)

        google_article = Post.objects.create(
           title='How to improve your Google rating?',
           created_by=jess,
           type='TU',
           content='Firstly, add the correct SEO tags...',
        )
        google_article.save()
        google_article.categories.add(seo_optimization)

        programming_article = Post.objects.create(
           title='Which programming language is the best?',
           created_by=jess,
           type='RS',
           content='The best programming languages are:\n1) Python\n2) Java\n3) C/C++...',
        )
        programming_article.save()
        programming_article.categories.add(programming)

        ubuntu_article = Post.objects.create(
           title='Installing the latest version of Ubuntu',
           created_by=johnny,
           type='TU',
           content="In this tutorial, we'll take a look at how to setup the latest version of Ubuntu. Ubuntu "
                   "(/ʊˈbʊntuː/ is a Linux distribution based on Debian and composed mostly of free and open-source"
                   " software. Ubuntu is officially released in three editions: Desktop, Server, and Core for "
                   "Internet of things devices and robots.",
        )
        ubuntu_article.save()
        ubuntu_article.categories.add(system_administration)

        django_article = Post.objects.create(
           title='Django REST Framework and Elasticsearch',
           created_by=johnny,
           type='TU',
           content="In this tutorial, we'll look at how to integrate Django REST Framework with Elasticsearch. "
           "We'll use Django to model our data and DRF to serialize and serve it. Finally, we'll index the data "
           "with Elasticsearch and make it searchable.",
        )
        django_article.save()
        django_article.categories.add(system_administration)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))