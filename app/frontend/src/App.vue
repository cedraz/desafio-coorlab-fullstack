<script setup>
  import { ref } from 'vue'
  import { getCities } from './api/get-cities'
  import { getTravels } from './api/get-travels'
  import travelCard from './components/travelCard.vue'
  import modalCard from './components/modalCard.vue'
  import { PhMathOperations, PhTruck, PhHandCoins } from "@phosphor-icons/vue";
  
  let wrongFormData = ref(false)
  let cities = ref([])
  let destiny = ref(null)
  let date = ref(null)

  let economic = ref({})
  let confort = ref({})

  async function renderCities() {
    cities.value = await getCities()
  }

  async function submit() {

    if (!destiny.value || !date.value) {
      wrongFormData.value = true
      return
    }

    const travels = await getTravels(destiny.value)

    economic.value = travels.economic
    confort.value = travels.confort
  }
  
  function handleClear() {
    economic.value = {}
    confort.value = {}
  }

  function handleCloseModal() {
    wrongFormData.value = false
  }
  
  renderCities()
  
</script>

<template>
  <section class="grid mx-auto grid-cols-12 h-screen">
    <div class="h-full col-span-12 md:col-span-3 bg-[#2a3040] px-5 py-10">
      <img class="w-[200px]" src="./assets/logo.png" alt="logo">
      
      <div class="mt-14 flex items-center gap-3">
        <ph-math-operations :size="32" color="#ffffff" />
        <h3 class="text-white text-xl"> Calculadora de viagens</h3>
      </div>
    </div>

    <div class="flex flex-col h-full col-span-12 md:col-span-9 bg-[#f8f8f8]">
      <div class="h-[80px] shadow-xl"></div>

      <div class="h-full w-full flex items-center justify-center px-10">
        <div class="w-full">
          <div class="flex gap-3 rounded-t-md h-[65px] w-full px-8 py-2 bg-[#2a3040] items-center">
            <ph-truck :size="32" color="#ffffff" />
            <h1 class="text-xl text-white font-bold">Calculadora de Viagem</h1>
          </div>

          <div class="rounded-b-md bg-white p-5 flex flex-col lg:flex-row gap-3 h-full">
            <div class="bg-[#f3f3f3] px-8 min-h-[300px] py-14 xl:w-[400px] gap-5 flex flex-col justify-center">
              <div class="flex gap-3" >
                <ph-hand-coins :size="32" color="#000000" />
                <h1 class="text-xl">Calcule o Valor da Viagem</h1>
              </div>

              <div class="flex flex-col">
                <label for="destiny" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Destino</label>
                <select 
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                  name="destiny" 
                  id="destiny"
                  v-model="destiny"
                >
                <option disabled :value="null">Data</option>
                  <option v-for="(city, index) in cities" :key="index" :value="city">{{ city }}</option>
                </select>
              </div>

              <div class="flex flex-col">
                <label for="destiny" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Selecione uma data</label>
                <input v-model="date" class="py-2 px-3" type="date" name="date" id="date" placeholder="Selecione uma data">
              </div>

              <button class="bg-[#04a8b2] text-[#ffffff] place-self-center py-2 px-16 rounded-md" @click="submit">Buscar</button>
            </div>
            <div class="w-full min-h-[300px] flex flex-col items-center justify-center">
              <h2 class="place-self-start text-xl mb-4" v-if="Object.keys(economic).length > 0">
                Estas são as melhores alternativas de viagem para a data selecionada
              </h2>
              <div class="flex flex-col gap-7 sm:gap-3 w-full" v-if="Object.keys(economic).length > 0">
                <travelCard :name="confort.name" :bed="confort.bed" :duration="confort.duration" :price="confort.price_conf" :seatType="'Leito'"/>

                <travelCard :name="economic.name" :bed="economic.seat" :duration="economic.duration" :price="economic.price_econ" :seatType="'Poltrona'"/>
              </div>
              <h1 v-else>Nenhum dado selecionado</h1>
              <button class="place-self-end mt-5 lg:mt-auto bg-[#e09835] rounded-md px-[70px] py-1" v-if="Object.keys(economic).length > 0" @click="handleClear">
                Limpar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <modalCard :wrongFormData="wrongFormData" :closeForm="handleCloseModal" />
</template>

