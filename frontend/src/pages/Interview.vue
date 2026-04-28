<script setup>

import Question from "@/components/Question.vue";
import Start from "@/components/Start.vue";
import {ref} from "vue";

const currentStep = ref('start') // 'start', 'question', 'result'
const currentQuestionData = ref(null)
const currentResultData = ref(null)

const handleInterviewResponse = (dataFromBackend) => {
  if (dataFromBackend.is_finished) {
    currentResultData.value = dataFromBackend.result
    currentStep.value = 'result'
  } else {
    currentQuestionData.value = dataFromBackend.question_response
    currentStep.value = 'question'
  }
}
</script>

<template>
  <div>
    <Start
      v-if="currentStep === 'start'"
      @started="handleInterviewResponse"
    />

    <Question
      v-else-if="currentStep === 'question'"
      :question-data="currentQuestionData"
      @answered="handleInterviewResponse"
    />
  </div>
</template>
