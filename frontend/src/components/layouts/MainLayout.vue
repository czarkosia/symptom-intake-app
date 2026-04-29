<script setup>
import Card from 'primevue/card'
</script>

<template>
  <div class="flex items-center justify-center w-full px-4 mt-12 mb-12">
    <Card class="w-full max-w-2xl shadow-xl bg-white  border border-brand-primary rounded-3xl overflow-hidden p-2">

      <template #title>
        <h2 class="text-2xl font-bold text-brand-dark mb-2 px-2">
          <slot name="title"></slot>
        </h2>
      </template>

      <template #content>
        <div class="px-2 mt-2">
          <slot name="content"></slot>
        </div>
      </template>

    </Card>
  </div>
</template>