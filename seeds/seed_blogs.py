import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_main.settings")
django.setup()

from blogs.models import Category, Blog
from django.contrib.auth.models import User



# ---------- GET AUTHOR ----------

author = User.objects.first()

if not author:
    raise Exception(
        "No users found. Create a superuser first using:\n"
        "python manage.py createsuperuser"
    )


# ---------- BLOG DATA ----------

blogs = [
{
"title": "The Importance of Strong Password Security",
"slug": "importance-of-strong-password-security",
"category": "Cybersecurity",
"short_description": "Strong passwords remain one of the simplest and most effective ways to protect personal and professional accounts from cyber threats.",
"blog_body": "Passwords are often the first line of defense against cybercriminals. Despite advances in security technologies, weak passwords continue to be a major cause of data breaches and account compromises. Many users still rely on simple passwords that are easy to remember but also easy to guess. Cybercriminals use automated tools that can test thousands of password combinations in seconds. A strong password should contain a combination of uppercase letters, lowercase letters, numbers, and special characters. It should also be unique for every account. Reusing passwords across multiple websites creates significant risk because a breach on one platform can expose accounts on many others. Password managers help users generate and store secure passwords without needing to memorize each one. Multi-factor authentication adds an additional layer of security by requiring another verification method. By adopting strong password practices, users can significantly reduce their chances of becoming victims of cybercrime."
},
{
"title": "Why HTML CSS and JavaScript Still Matter",
"slug": "why-html-css-and-javascript-still-matter",
"category": "Web Development",
"short_description": "Modern frameworks come and go, but HTML, CSS, and JavaScript remain the foundation of every website on the internet.",
"blog_body": "Every website is built upon three core technologies: HTML, CSS, and JavaScript. HTML provides structure, CSS controls appearance, and JavaScript adds interactivity. While modern frameworks such as React, Angular, and Vue receive significant attention, they all rely on these core technologies. Understanding HTML allows developers to create meaningful page structures and improve accessibility. CSS enables responsive layouts, animations, and attractive user interfaces. JavaScript powers dynamic behavior, from form validation to complex web applications. Developers who master these fundamentals can adapt to new frameworks much more easily. Many beginners make the mistake of jumping directly into advanced libraries without understanding the basics. This often creates gaps in knowledge that become problematic later. Learning HTML, CSS, and JavaScript thoroughly provides a strong foundation for future growth in web development and remains one of the best investments for aspiring developers."
},
{
"title": "Frontend vs Backend Development",
"slug": "frontend-vs-backend-development",
"category": "Web Development",
"short_description": "Understanding the difference between frontend and backend development helps beginners choose the right path in software development.",
"blog_body": "Web development is generally divided into two major areas: frontend and backend development. Frontend development focuses on what users see and interact with directly. It involves creating layouts, designing interfaces, and improving user experiences using technologies such as HTML, CSS, and JavaScript. Backend development focuses on the server side of applications. Backend developers manage databases, APIs, authentication systems, and business logic using languages such as Python, Java, PHP, or Node.js. Both roles are essential for building modern applications. Frontend developers ensure that websites look appealing and function smoothly, while backend developers ensure that data is processed correctly and securely. Full-stack developers combine skills from both areas. For beginners, exploring both frontend and backend development can help identify personal interests and career goals."
},
{
"title": "Building Responsive Websites in 2026",
"slug": "building-responsive-websites-in-2026",
"category": "Web Development",
"short_description": "Responsive web design ensures that websites provide excellent user experiences across desktops, tablets, and smartphones.",
"blog_body": "Internet users access websites from a wide variety of devices. Responsive design ensures that websites adapt automatically to different screen sizes and resolutions. Modern web developers rely on flexible layouts, media queries, and responsive units to create interfaces that work consistently across devices. Mobile-first development has become a popular approach because smartphones generate a significant portion of web traffic worldwide. Responsive design improves usability, accessibility, and search engine rankings. Visitors are more likely to stay on websites that display correctly on their devices. Poor mobile experiences often lead to higher bounce rates and lower engagement. By prioritizing responsive design, developers create websites that are more accessible, professional, and future-proof."
},
{
"title": "Understanding REST APIs for Beginners",
"slug": "understanding-rest-apis-for-beginners",
"category": "Web Development",
"short_description": "REST APIs allow applications to communicate with each other and form the backbone of modern web development.",
"blog_body": "REST APIs have become a standard method for communication between software applications. API stands for Application Programming Interface, while REST stands for Representational State Transfer. A REST API allows one application to request data or services from another using HTTP methods such as GET, POST, PUT, and DELETE. For example, a weather application may request forecast information from a weather service API. Modern web applications often separate frontend and backend systems, making APIs essential for data exchange. Understanding REST APIs helps developers build scalable applications and integrate third-party services. Learning concepts such as endpoints, requests, responses, status codes, and authentication is crucial for aspiring web developers. REST APIs continue to play a major role in modern software architecture."
},
{
"title": "Why Python Remains the Most Popular Programming Language",
"slug": "why-python-remains-popular",
"category": "Programming",
"short_description": "Python continues to dominate the programming world due to its simplicity, versatility, and massive ecosystem of libraries and frameworks.",
"blog_body": "Python has established itself as one of the most widely used programming languages in the world. Its simple syntax allows beginners to focus on problem-solving rather than complicated language rules. At the same time, Python is powerful enough to support large-scale applications used by major organizations. The language is popular in web development, data science, machine learning, automation, cybersecurity, and scientific computing. Frameworks such as Django and Flask simplify web development, while libraries like NumPy, Pandas, and TensorFlow support advanced analytics and artificial intelligence projects. Python's large community contributes thousands of open-source packages, making it easier for developers to solve complex problems efficiently. The language also enjoys strong educational support, making it a common choice for universities and online learning platforms. As technology continues to evolve, Python remains relevant because of its flexibility and ability to adapt to emerging fields. For students entering the technology industry, learning Python can open doors to numerous career opportunities."
},
{
"title": "Understanding Data Structures and Algorithms",
"slug": "understanding-data-structures-and-algorithms",
"category": "Programming",
"short_description": "Data structures and algorithms form the foundation of efficient software development and technical problem solving.",
"blog_body": "Data structures and algorithms are among the most important concepts in computer science. Data structures provide ways to organize and store information efficiently, while algorithms define the steps needed to solve problems. Common data structures include arrays, linked lists, stacks, queues, trees, and hash tables. Each structure offers unique advantages depending on the problem being solved. Algorithms such as sorting, searching, and graph traversal help developers process data effectively. Understanding time complexity and space complexity allows programmers to evaluate the performance of different solutions. Companies often assess DSA knowledge during technical interviews because it demonstrates analytical thinking and problem-solving ability. While mastering these concepts requires practice, they provide long-term benefits that extend far beyond interview preparation. Strong DSA knowledge enables developers to build scalable, efficient, and reliable software systems."
},
{
"title": "The Benefits of Learning C Programming",
"slug": "benefits-of-learning-c-programming",
"category": "Programming",
"short_description": "C programming remains one of the best languages for understanding how computers and software work at a deeper level.",
"blog_body": "Although many modern programming languages offer higher-level abstractions, C remains highly valuable for learning computer science fundamentals. C provides direct access to memory through pointers, helping developers understand how programs interact with hardware. Operating systems, embedded systems, databases, and many performance-critical applications are built using C. Learning C develops a strong understanding of memory management, data structures, and low-level programming concepts. These skills make it easier to learn other languages later. Many universities continue to teach C because it exposes students to important programming principles that are often hidden in modern languages. While beginners may find C challenging at first, the knowledge gained provides a solid foundation for advanced software development and systems programming."
},
{
"title": "How Data Science Helps Businesses Grow",
"slug": "how-data-science-helps-businesses-grow",
"category": "Data Science",
"short_description": "Data science enables organizations to transform raw information into actionable insights that drive business growth.",
"blog_body": "Modern businesses generate enormous amounts of data through customer interactions, transactions, and operational processes. Data science helps organizations extract meaningful insights from this information. By analyzing historical trends and identifying patterns, businesses can make more informed decisions. Data scientists use tools such as Python, SQL, and machine learning algorithms to uncover valuable information hidden within large datasets. Applications include customer segmentation, sales forecasting, fraud detection, and recommendation systems. Organizations that effectively use data can improve efficiency, reduce costs, and enhance customer satisfaction. As competition increases across industries, data-driven decision making has become a critical factor for success. Data science continues to play an important role in helping companies understand their customers and respond more effectively to market changes."
},
{
"title": "Understanding Data Visualization",
"slug": "understanding-data-visualization",
"category": "Data Science",
"short_description": "Data visualization transforms complex datasets into clear visual representations that improve understanding and decision making.",
"blog_body": "Raw data can be difficult to interpret, especially when dealing with large datasets. Data visualization addresses this challenge by presenting information through charts, graphs, dashboards, and other visual formats. Effective visualizations allow users to identify patterns, trends, and anomalies quickly. Businesses use data visualization to monitor performance, track key metrics, and communicate findings to stakeholders. Tools such as Tableau, Power BI, and Python visualization libraries have made it easier than ever to create compelling visual reports. Good visualization design focuses on clarity, simplicity, and accuracy. Poorly designed charts can mislead audiences and obscure important information. As organizations become increasingly data-driven, the ability to communicate insights visually has become a valuable skill for analysts, managers, and decision makers alike."
},
{
"title": "The Rise of Big Data Analytics",
"slug": "rise-of-big-data-analytics",
"category": "Data Science",
"short_description": "Big Data Analytics helps organizations uncover patterns, trends, and opportunities from massive volumes of information.",
"blog_body": "The amount of data generated globally continues to grow at an unprecedented rate. Every online purchase, social media interaction, and digital transaction contributes to an expanding pool of information. Big Data Analytics refers to the process of examining large and complex datasets to identify meaningful insights. Organizations use these insights to improve products, understand customer behavior, and optimize business operations. Modern technologies such as cloud computing, distributed databases, and machine learning have made it possible to process vast amounts of information efficiently. Industries including healthcare, finance, retail, and transportation rely heavily on big data solutions. Companies that leverage data effectively gain a competitive advantage by making faster and more informed decisions. As digital transformation continues, big data analytics will remain a critical driver of innovation and growth."
},
{
"title": "Building a Successful Career in Technology",
"slug": "building-successful-career-in-technology",
"category": "Career & Learning",
"short_description": "Success in technology requires continuous learning, practical experience, and the ability to adapt to changing industry trends.",
"blog_body": "The technology industry offers countless opportunities for individuals willing to learn and grow. Building a successful career begins with developing strong technical foundations and gaining practical experience through projects. Employers increasingly value skills demonstrated through portfolios and real-world work rather than relying solely on academic qualifications. Continuous learning is essential because technologies evolve rapidly. Professionals must stay updated with industry trends, tools, and best practices. Networking also plays an important role in career development. Connecting with peers, mentors, and industry professionals can create opportunities for growth and collaboration. Soft skills such as communication, teamwork, and problem-solving are equally important. A balanced combination of technical expertise and professional skills enables individuals to thrive in competitive technology environments. Long-term success comes from persistence, adaptability, and a commitment to lifelong learning."
},
{
"title": "How Students Can Build a Strong Portfolio",
"slug": "how-students-can-build-a-strong-portfolio",
"category": "Career & Learning",
"short_description": "A well-structured portfolio demonstrates practical skills and helps students stand out during internships and job applications.",
"blog_body": "A portfolio serves as evidence of a student's abilities and accomplishments. While resumes describe skills, portfolios demonstrate them through actual projects and achievements. Students can begin by creating small projects that showcase their interests and technical capabilities. Web applications, programming challenges, data analysis projects, and open-source contributions are excellent additions to a portfolio. Quality is often more important than quantity. A few well-documented projects can create a stronger impression than numerous unfinished ones. Students should explain the problem each project solves, the technologies used, and the lessons learned during development. Hosting projects online through platforms such as GitHub makes them easily accessible to recruiters. A strong portfolio reflects dedication, creativity, and problem-solving ability, making it one of the most valuable assets for students entering the technology industry."
},
{
"title": "Top Technology Trends to Watch in 2026",
"slug": "top-technology-trends-to-watch-in-2026",
"category": "Technology",
"short_description": "Artificial intelligence, cloud computing, cybersecurity, and automation continue to shape the future of technology worldwide.",
"blog_body": "Technology evolves rapidly, creating new opportunities and challenges each year. In 2026, artificial intelligence remains one of the most influential technologies, driving innovation across industries. Cloud computing continues to enable scalable and flexible digital services for businesses of all sizes. Cybersecurity has become increasingly important as organizations work to protect sensitive data and critical infrastructure from evolving threats. Automation technologies are improving efficiency in manufacturing, logistics, and customer service operations. Edge computing is gaining momentum by processing data closer to users and devices, reducing latency and improving performance. Sustainable technology solutions are also receiving increased attention as organizations seek environmentally responsible practices. Understanding emerging trends helps professionals and businesses prepare for future opportunities and maintain a competitive advantage in an increasingly digital world."
},
{
"title": "How AI Is Transforming Modern Healthcare",
"slug": "how-ai-is-transforming-modern-healthcare",
"category": "Artificial Intelligence",
"short_description": "Artificial intelligence is improving diagnosis, treatment planning, and patient care across healthcare systems worldwide.",
"blog_body": "Artificial intelligence is revolutionizing healthcare by helping medical professionals make faster and more accurate decisions. Machine learning algorithms can analyze medical images, detect abnormalities, and assist in diagnosing diseases at earlier stages. AI-powered systems also support treatment planning by evaluating patient data and identifying personalized care options. Hospitals use predictive analytics to optimize resource allocation and improve operational efficiency. Virtual health assistants provide patients with information, appointment scheduling, and medication reminders. While AI offers significant benefits, challenges related to privacy, ethics, and regulatory compliance remain important considerations. Healthcare organizations must ensure that AI systems are transparent, reliable, and secure. As technology continues to advance, artificial intelligence is expected to play an even greater role in improving healthcare outcomes and enhancing patient experiences."
}



]


# ---------- INSERT BLOGS ----------

for blog in blogs:

    category = Category.objects.get(
        category_name=blog["category"]
    )

    Blog.objects.get_or_create(
        slug=blog["slug"],
        defaults={
            "title": blog["title"],
            "category": category,
            "author": author,
            "featured_image": "uploads/default.jpg",
            "short_description": blog["short_description"],
            "blog_body": blog["blog_body"],
            "status": "Published",
        }
    )

print("Blogs inserted successfully.")