<script setup>
import { ref, reactive } from 'vue'
import MainLayout from "@/components/layouts/MainLayout.vue"
import InputNumber from 'primevue/inputnumber'
import Select from 'primevue/select'
import Textarea from 'primevue/textarea'
import Button from 'primevue/button'
import Message from 'primevue/message'

import { AGE_UNITS, SEX_OPTIONS } from "@/const/demographics.js";
import {startInterviewCall} from "@/api/api.js";

const emit = defineEmits(['started'])

const form = reactive({
  age: null,
  age_unit: 'year',
  sex: '',
  text: ''
})

const isLoading = ref(false)
const errorMessage = ref('')

const validateForm = () => {
  if (!form.age) return "Please input your age."
  if (!form.sex) return "Please input your sex."
  if (!form.text.trim()) return "Describe your symptoms."
  return null
}

const submitInterview = async () => {
  errorMessage.value = ''

  const validationError = validateForm()
  if (validationError) {
    errorMessage.value = validationError
    return
  }

  isLoading.value = true

  const baseUrl = import.meta.env.VITE_BACKEND_URI;
  try {
    const data = await startInterviewCall(form)
    emit('started', data)

  } catch (error) {
    errorMessage.value = error.message || 'Connection failed.'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <MainLayout>
    <template #title>
      Start your medical interview
    </template>

    <template #content>
      <form @submit.prevent="submitInterview" class="flex flex-col gap-6 mt-2 px-2">

        <div class="flex flex-col sm:flex-row gap-6">

          <div class="flex flex-col gap-2 sm:w-1/3">
            <label class="font-semibold text-gray-700">Sex <span class="text-red-500">*</span></label>
            <Select
              v-model="form.sex"
              :options="SEX_OPTIONS"
              optionLabel="label"
              optionValue="value"
              placeholder="Choose sex..."
              class="w-full border border-gray-300 rounded-lg flex items-center px-2 py-1"
              required
            />
          </div>

          <div class="flex flex-col gap-2 sm:w-2/3">
            <label class="font-semibold text-gray-700">Age <span class="text-red-500">*</span></label>
            <div class="flex gap-3">
              <InputNumber
                v-model="form.age"
                :min="0" :max="130"
                placeholder="e.g. 30"
                class="flex-1"
                inputClass="w-full border border-gray-300 rounded-lg p-3 focus:!ring-2 focus:!ring-brand-primary outline-none transition-all"
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
          <label class="font-semibold text-gray-700">Provide your symptoms description <span class="text-red-500">*</span></label>
          <Textarea
            v-model="form.text"
            rows="4"
            autoResize
            placeholder="I have had a strong headache since yesterday..."
            class="w-full border border-gray-300 rounded-lg p-3 focus:!ring-2 focus:!ring-brand-primary outline-none transition-all"
            required
          />
        </div>

        <Button
          type="submit"
          label="Start interview"
          :loading="isLoading"
          class="w-full mt-4 !bg-brand-primary hover:!bg-brand-dark text-white font-bold py-3 rounded-xl transition-colors !border-none"
          size="large"
        />

        <Message v-if="errorMessage" severity="error" :closable="false" class="mt-2">
          {{ errorMessage }}
        </Message>

      </form>
    </template>
  </MainLayout>
</template>