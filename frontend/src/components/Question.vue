<script setup>
import Button from 'primevue/button'
import MainLayout from "@/components/layouts/MainLayout.vue";
import {ref} from "vue";

const answered = defineEmits(['answered'])

const questionText = ref("Do you have any of these symptoms?")
const symptoms = ref([
  { id: 's_1193', name: 'Strong headache' },
  { id: 's_1194', name: 'Dizziness' }
])

const answers = ref({})

const setAnswer = (itemId, choice) => {
  answers[itemId] = choice
}

const submitAnswers = async () => {
  const answeredCount = Object.keys(answers).length
  if (answeredCount < symptoms.value.length) {
    alert("Please answer all the questions before you submit anything.")
    return
  }

  console.log("Zebrane odpowiedzi:", answers.value)
  // TODO: Send patients response to backend

  // router.push('/result') // Tymczasowe przejście do wyników
}
</script>

<template>
  <MainLayout>
    <template #title>
      {{ questionText }}
    </template>

    <template #content>
      <div class="flex flex-col gap-6">

        <div v-for="item in symptoms" :key="item.id" class="flex flex-col gap-3 pb-4 border-b border-gray-100 last:border-0">
          <p class="font-semibold text-gray-800 text-lg">{{ item.name }}</p>

          <div class="flex flex-wrap gap-2 sm:flex-nowrap">
            <Button
              label="Yes"
              icon="pi pi-check"
              :outlined="answers[item.id] !== 'present'"
              @click="setAnswer(item.id, 'present')"
              class="flex-1"
            />
            <Button
              label="No"
              icon="pi pi-times"
              :outlined="answers[item.id] !== 'absent'"
              @click="setAnswer(item.id, 'absent')"
              severity="danger"
              class="flex-1"
            />
            <Button
              label="I don't know"
              icon="pi pi-question"
              :outlined="answers[item.id] !== 'unknown'"
              @click="setAnswer(item.id, 'unknown')"
              severity="secondary"
              class="flex-1"
            />
          </div>
        </div>

        <Button
          label="Submit answer"
          class="w-full mt-4"
          size="large"
          @click="submitAnswers"
        />

      </div>
    </template>
  </MainLayout>
</template>