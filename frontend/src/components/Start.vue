<script setup>
import { ref, reactive } from 'vue'
import Card from 'primevue/card'
import InputNumber from 'primevue/inputnumber'
import Select from 'primevue/select'
import Textarea from 'primevue/textarea'
import Button from 'primevue/button'
import Message from 'primevue/message'
import {AGE_UNITS, SEX_OPTIONS} from "@/const/demographics.js";

const form = reactive({
  age: null,
  age_unit: 'year',
  sex: '',
  text: ''
})

const isLoading = ref(false)
const errorMessage = ref('')

const submitInterview = async () => {
  errorMessage.value = ''
  isLoading.value = true

  try {
    const response = await $fetch('http://localhost:8000/api/v1/interview/start', {
      method: 'POST',
      body: form
    })

    console.log("Response:", response)
    // TODO: Navigate to further questions or results page

  } catch (error) {
    errorMessage.value = error.data?.message || 'Internal server error'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="flex items-center justify-center w-full px-4 mt-12 mb-12">

    <Card class="w-full max-w-2xl shadow-md bg-white border border-brand-dark rounded-3xl overflow-hidden p-2">
      <template #title>
        <h2 class="text-2xl font-bold text-brand-dark mb-2 px-2">Start your medical interview</h2>
      </template>

      <template #content>
        <form @submit.prevent="submitInterview" class="flex flex-col gap-6 mt-2 px-2">

          <div class="flex flex-col sm:flex-row gap-6">

            <div class="flex flex-col gap-2 sm:w-1/3">
              <label class="font-semibold text-gray-700">Sex</label>
              <Select
                v-model="form.sex"
                :options="SEX_OPTIONS"
                optionLabel="label"
                optionValue="value"
                placeholder="Choose sex..."
                class="w-full border border-gray-300 rounded-lg flex items-center px-2 py-1"
              />
            </div>

            <div class="flex flex-col gap-2 sm:w-2/3">
              <label class="font-semibold text-gray-700">Age</label>
              <div class="flex gap-3">
                <InputNumber
                  v-model="form.age"
                  :min="0" :max="130"
                  placeholder="np. 30"
                  class="flex-1"
                  inputClass="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-primary outline-none transition-all"
                />
                <Select
                  v-model="form.age_unit"
                  :options="AGE_UNITS"
                  optionLabel="label"
                  optionValue="value"
                  class="w-40 border border-gray-300 rounded-lg flex items-center px-2"
                />
              </div>
            </div>

          </div>

          <div class="flex flex-col gap-2">
            <label class="font-semibold text-gray-700">Provide your symptoms description</label>
            <Textarea
              v-model="form.text"
              rows="4"
              autoResize
              placeholder="I have had a strong headache since yesterday..."
              class="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-brand-primary outline-none transition-all"
            />
          </div>

          <Button
            type="submit"
            label="Start interview"
            :loading="isLoading"
            class="w-full mt-4 !bg-brand-primary !hover:bg-brand-dark text-white font-bold py-3 rounded-xl transition-colors !border-none"
            size="large"
          />

          <Message v-if="errorMessage" severity="error" :closable="false">
            {{ errorMessage }}
          </Message>

        </form>
      </template>
    </Card>
  </div>
</template>