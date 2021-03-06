from django.conf import settings

from jab.models import Post, SidebarItem


def add_blog_settings(context):
    return {
        'blog_name': getattr(settings, "BLOG_NAME", ""),
        'blog_description': getattr(settings, "BLOG_DESCRIPTION", ""),
        'blog_author': getattr(settings, "BLOG_AUTHOR", ""),
        'blog_author_email': getattr(settings, "BLOG_AUTHOR_EMAIL", ""),
        'blog_author_twitter': getattr(settings, "BLOG_AUTHOR_TWITTER", ""),
    }


def add_header_links(context):
    return {
        "posts_in_header": Post.published_posts().filter(link_from_header=True)
    }


def add_sidebar_items(context):
    return {
        "sidebar_items": SidebarItem.objects.all(),
    }
