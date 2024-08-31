# static-site-generator ♺

![architecture](/public/staticsitegenerator_infrastructure.png)

## 💻 A program to covert markdowns into a static website.

The flow of data through the full system:

1. Markdown files are in the `/content` directory. A `template.html` file is in the root of the project.
2. The static site generator (the Python code in `src/`) reads the Markdown files and the template file.
3. The generator converts the Markdown files to a final HTML file for each page and writes them to the `/public` directory.
4. Start the built-in Python HTTP server (a separate program, unrelated to the generator) to serve the contents of the /public directory on `http://localhost:8888` (our local machine).
5. We open a browser and navigate to `http://localhost:8888` to view the rendered site.
