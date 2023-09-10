from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "yoko"
        return ctxt
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = "1233442523"
        ctxt["skills"] = [
            "python",
            "C++",
            "Javascript",
            "Rust",
            "Go",
        ]
        return ctxt