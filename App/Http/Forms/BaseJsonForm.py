from django import forms
from App.Core.settings import DEBUG
 
 
class BaseJsonForm(forms.Form):
 
    def get_parameter_information(self):
        information_list = []
        for name in self.fields.keys():
            str_value = self[name].__str__()
            values = str_value.split(' ')
            str_value = ','.join(values[1:-1])
            information_list.append({name: str_value})
        return str(information_list).replace('\"', '')
 
    def get_errors_information(self):
        errors = self.errors.as_json()
        errors_dict = eval(errors)
        errors_str = ''
        for key, value in errors_dict.items():
            errors_str += key + ' ' + value[0].get('message')
        return str(errors_str)
 
    def errors_information(self):
        if self.errors:
            if DEBUG:
                parameter_information =   self.get_parameter_information()
                message = self.get_errors_information()
            else:
                parameter_information = []
                message= 'Parameter exception'
            response = {'error': message, 'format': parameter_information}
            return response
        else:
            return None