from blog_extra.models import About

About.objects.get_or_create(
  about_heading = "About Us",
  about_description = "This blog is a platform for students, aspiring developers, and technology enthusiasts who want to learn modern technology in a simple and practical way. We publish articles on programming, web development, artificial intelligence, cybersecurity, data science, and career development. Our mission is to make technology education accessible, helping readers build skills, create projects, and stay updated with industry trends while preparing for successful careers in the IT field."
)

print("About created successfully")