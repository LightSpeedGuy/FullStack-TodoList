from rest_framework import serializers

from .models import Todo, TodoType, SubTodo


class SubTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTodo
        fields = ['id', 'title', 'is_done']

    def create(self, validated_data):
        todo_id = self.context['todo_id']
        related_todo = Todo.objects.get(pk=todo_id)
        return SubTodo.objects.create(**validated_data, todo=related_todo)


class TodoSerializer(serializers.ModelSerializer):
    is_removed = serializers.BooleanField(write_only=True)
    sub_todos = SubTodoSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at',
                  'deadline', 'is_finished_before_deadline', 'status', 'is_removed', 'sub_todos', 'todo_type']

    def create(self, validated_data):
        user = self.context['user']
        return Todo.objects.create(**validated_data, user=user)


class TodoTypeSerializer(serializers.ModelSerializer):
    is_removed = serializers.BooleanField(write_only=True)

    class Meta:
        model = TodoType
        fields = ['id', 'label', 'is_removed']

    def create(self, validated_data):
        user = self.context['user']
        return TodoType.objects.create(**validated_data, user=user)