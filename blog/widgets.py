from django import forms


class CounterTextInput(forms.TextInput):
    template_name = 'widgets/counter_text.html'



class RateitjsWidget(forms.NumberInput):
    input_type = 'rating'
    template_name = 'widgets/rateitjs_number.html'

    class Media:
        css = {
            'all' : [
                'widgets/rateit.js/rateit.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            ''
        ]

class TuiEditorWidget(forms.Textarea):
    template_name = 'widgets/tui-editor_widget.html'

    class Media:
        css = {
            'all': [
                'codemirror/lib/codemirror.css',
                'highlightjs/styles/github.css',
                'tui-editor/dist/tui-editor.css',
                'tui-editor/dist/tui-editor-contents.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            'tui-code-snippet/dist/tui-code-snippet.js',
            'markdown-it/dist/markdown-it.js',
            'to-mark/dist/to-mark.js',
            'codemirror/lib/codemirror.js',
            'highlightjs/highlight.pack.js',
            'squire-rte/build/squire.js',
            'tui-editor/dist/tui-editor-Editor.min.js',
            'tui-editor/dist/tui-editor-extScrollSync.js',
            'tui-editor/dist/tui-editor-extUML.js'

        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['style'] = 'display: none;'
        return attrs
