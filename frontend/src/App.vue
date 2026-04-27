<script setup>

import {ref} from "vue";
import Start from "@/components/Start.vue";
import Question from "@/components/Question.vue";
import NotFoundBanner from "@/components/banners/NotFoundBanner.vue";

const currentPath = window.location.pathname
const currentStep = ref('start') // 'start', 'question', 'result'
const currentQuestionData = ref(null)
const currentResultData = ref(null)

const handleInterviewResponse = (dataFromBackend) => {
  if (dataFromBackend.is_finished) {
    currentResultData.value = dataFromBackend.result
    currentStep.value = 'result'
  } else {
    // Jeśli są kolejne pytania:
    currentQuestionData.value = dataFromBackend.question_response
    currentStep.value = 'question'
  }
}

</script>

<template>
  <div class="min-h-screen bg-medical-surface">
    <NotFoundBanner v-if="currentPath !== '/'" />

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
