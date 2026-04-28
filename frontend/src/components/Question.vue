<script setup>
import { ref } from "vue";
import Button from 'primevue/button'
import Message from 'primevue/message'
import MainLayout from "@/components/layouts/MainLayout.vue";
import { answerQuestionCall } from "@/api/api.js";

const props = defineProps({
  questionData: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['answered'])

const selectedChoice = ref(null)
const isLoading = ref(false)
const errorMessage = ref('')

const submitAnswer = async () => {
  if (!selectedChoice.value) {
    errorMessage.value = "Please select an answer."
    return
  }

  errorMessage.value = ''
  isLoading.value = true

  try {
    const payload = {
      item_id: props.questionData.item_id,
      choice_id: selectedChoice.value
    }

    const data = await answerQuestionCall(payload)
    emit('answered', data)

  } catch (error) {
    console.error("Request error:", error)
    errorMessage.value = error.message || 'Connection failed.'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <MainLayout>
    <template #title>
      {{ questionData.question_text }}
    </template>

    <template #content>
      <div class="flex flex-col gap-6">

        <div class="flex flex-col gap-4 pb-4">

          <div class="flex flex-col sm:flex-row flex-wrap gap-3 justify-center mt-2">
            <Button
              v-for="choice in questionData.choices"
              :key="choice.id"
              :label="choice.label"
              :outlined="selectedChoice !== choice.id"
              @click="selectedChoice = choice.id"
              class="flex-1"
            />
          </div>
        </div>

        <Button
          label="Submit answer"
          class="w-full mt-2 !bg-brand-primary hover:!bg-brand-dark text-white font-bold py-3 rounded-xl transition-colors !border-none"
          size="large"
          :loading="isLoading"
          @click="submitAnswer"
        />

        <Message v-if="errorMessage" severity="error" :closable="false" class="mt-2">
          {{ errorMessage }}
        </Message>

      </div>
    </template>
  </MainLayout>
</template>