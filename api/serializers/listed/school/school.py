from ...name import SchoolNameSerializer

class SchoolSerializer(SchoolNameSerializer):
  class Meta(SchoolNameSerializer.Meta):
    fields = SchoolNameSerializer.Meta.fields + ['address', 'website', 'lang', 'type', 'profiles', 'start_grade', 'final_grade']