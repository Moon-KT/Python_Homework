class Developer:
    def __init__(self, dev_id, name, dob, exp_year):
        self.dev_id = dev_id
        self.name = name
        self.dob = dob
        self.exp_year = exp_year


class Frontend(Developer):
    def __init__(self, dev_id, name, dob, exp_year, html_level, css_level, js_level):
        super().__init__(dev_id, name, dob, exp_year)
        self.html_level = html_level
        self.css_level = css_level
        self.js_level = js_level

    def __str__(self):
        return f"Frontend Developer: {self.name}, HTML: {self.html_level}, CSS: {self.css_level}, JS: {self.js_level}"


class Backend(Developer):
    def __init__(self, dev_id, name, dob, exp_year, sql_level, java_level, spring_level):
        super().__init__(dev_id, name, dob, exp_year)
        self.sql_level = sql_level
        self.java_level = java_level
        self.spring_level = spring_level

    def __str__(self):
        return f"Backend Developer: {self.name}, SQL: {self.sql_level}, Java: {self.java_level}, Spring: {self.spring_level}"


class Fullstack:
    def __init__(self, frontend: Frontend, backend: Backend):
        self.frontend = frontend
        self.backend = backend

    def __str__(self):
        return f"Fullstack Developer: {self.frontend.name}\nFrontend Skills: HTML - {self.frontend.html_level}, " \
               f"CSS - {self.frontend.css_level}, JS - {self.frontend.js_level}\nBackend Skills: " \
               f"SQL - {self.backend.sql_level}, Java - {self.backend.java_level}, Spring - {self.backend.spring_level}"


# Creating instances of Frontend and Backend
frontend_instance = Frontend(1, 'John Doe', '01-01-1990', 5, 'Intermediate', 'Advanced', 'Intermediate')
backend_instance = Backend(2, 'Jane Smith', '12-05-1985', 7, 'Advanced', 'Intermediate', 'Intermediate')

# Creating an instance of Fullstack
fullstack_dev = Fullstack(frontend_instance, backend_instance)

# Printing the Fullstack object will invoke its __str__() method
print(fullstack_dev)
