<script setup>
const props = defineProps({
  name: String,
  bed: String,
  duration: String,
  price: String,
  seatType: String,
})

let price_in_reais = (props.price / 100).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

import { PhHandCoins, PhTimer } from "@phosphor-icons/vue";

</script>

<template>
  <div class="grid grid-cols-12 gap-3">
    <div class="col-span-12 sm:col-span-8 grid grid-cols-12 w-full">
      <div class="flex items-center justify-center rounded-s-md col-span-3 bg-[#04a8b2] px-2 py-4">
        <ph-hand-coins v-if="props.seatType === 'Leito'" :size="48" color="#ffffff" />
        <ph-timer v-else :size="48" color="#ffffff" />
      </div>

      <div class="pl-10 rounded-e-md col-span-9 bg-[#e2e2e2] px-2 py-4">
        <h3 class="font-bold text-lg"> {{ props.name }}</h3>
        <p> {{ props.seatType }}: {{ props.bed }} ( {{ props.seatType === 'Leito' ? 'Completo' : 'Convencional' }} )</p>
        <p> Tempo estimado: {{ props.duration }}</p>
      </div>
    </div>

    <div class="col-span-12 sm:col-span-4 rounded-md flex flex-col gap-3 justify-center bg-[#e2e2e2] ps-5 py-4">
      <p class="font-bold text-md">Preço</p>
      <p>{{ price_in_reais }}</p>
    </div>
  </div>
</template>
