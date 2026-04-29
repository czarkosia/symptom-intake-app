<script setup>
import Question from "@/components/Question.vue";
import Start from "@/components/Start.vue";
import { ref } from "vue";
import Results from "@/components/Results.vue";

const currentStep = ref('start')
const currentQuestionData = ref(null)
const currentResultData = ref(null)
const currentInterviewId = ref(null)

const handleRestart = () => {
  currentStep.value = 'start'
}

const handleInterviewResponse = (dataFromBackend) => {
  currentInterviewId.value = dataFromBackend.interview_id

  if (dataFromBackend.is_finished) {
    currentResultData.value = dataFromBackend
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
      :key="currentQuestionData.item_id"
      :interview-id="currentInterviewId"
      :question-data="currentQuestionData"
      @answered="handleInterviewResponse"
    />

    <Results
      v-else-if="currentStep === 'result'"
      :result-data="currentResultData"
      @restart="handleRestart"
    />
  </div>
</template>