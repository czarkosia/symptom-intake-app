<script setup>

import MainLayout from "@/components/layouts/MainLayout.vue";
import {computed} from "vue";
import {TRIAGE_LEVELS} from "@/const/triage.js";
import Button from 'primevue/button';
import ProgressBar from 'primevue/progressbar';

const props = defineProps({
  resultData: {
    type: Object,
    required: true,
  },
})
const emit = defineEmits(['restart'])
const restart = () => {
  emit('restart')
}

const formatProbability = (prob) => {
  return Math.round(prob * 100)
}

const triageConfig = computed(() => {
  const level = props.resultData.final_response?.triage_level
  return TRIAGE_LEVELS[level] || { label: 'Unknown recommendation', color: 'bg-gray-100 text-gray-800 border-gray-300', icon: 'pi-info-circle' }
})
const conditions = computed(() => {
  return props.resultData.final_response?.conditions || []
})

</script>

<template>
  <MainLayout>
    <template #title>
      Interview Results
    </template>

    <template #content>
      <div class="flex flex-col gap-8">

        <div class="flex flex-col gap-2">
          <h3 class="font-semibold text-gray-700 text-lg">Recommendation</h3>
          <div
            class="flex items-center gap-4 p-4 rounded-xl border-2"
            :class="triageConfig.color"
          >
            <i class="pi text-2xl" :class="triageConfig.icon"></i>
            <span class="font-bold text-lg">{{ triageConfig.label }}</span>
          </div>
        </div>

        <div class="flex flex-col gap-4">
          <h3 class="font-semibold text-gray-700 text-lg">Possible conditions</h3>

          <div v-if="conditions.length === 0" class="text-gray-500 italic">
            No specific conditions could be identified based on the provided symptoms.
          </div>

          <div
            v-for="condition in conditions"
            :key="condition.id"
            class="flex flex-col gap-2 p-4 border border-gray-200 rounded-xl bg-gray-50"
          >
            <div class="flex justify-between items-center">
              <span class="font-bold text-brand-dark">{{ condition.name }}</span>
              <span class="font-semibold text-gray-600">{{ formatProbability(condition.probability) }}%</span>
            </div>
            <ProgressBar
              :value="formatProbability(condition.probability)"
              :showValue="false"
              style="height: 8px"
            />
          </div>
        </div>

        <Button
          label="Start a new interview"
          class="w-full mt-4"
          size="large"
          outlined
          @click="restart"
        />

      </div>
    </template>
  </MainLayout>
</template>
