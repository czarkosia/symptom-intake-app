<script setup>
import Button from 'primevue/button'


// TODO: navigate to root page
const goHome = () => {}

</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-medical-surface px-4">
    <div class="text-center max-w-lg">
      <h1 class="text-9xl font-extrabold text-brand-primary tracking-widest drop-shadow-sm">
        404
      </h1>

      <h2 class="text-3xl font-bold text-brand-dark mt-6">
        Page Not Found
      </h2>

      <p class="text-gray-500 mt-4 mb-10 text-lg">
        It seems that you've got lost. Help me get you back on track!
      </p>

      <Button
        label="Go to home page"
        @click="goHome"
        class="!bg-brand-primary hover:!bg-brand-dark !border-none px-8 py-4 rounded-xl text-white font-bold text-lg shadow-lg hover:shadow-xl transition-all"
      />
    </div>
  </div>
</template>