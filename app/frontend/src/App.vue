<script setup>
  import { ref } from 'vue'
  import { getCities } from './api/get-cities'
  import { getTravels } from './api/get-travels'

  let cities = ref([])
  let destiny = ref('')

  let economic = ref({
    name: '',
    price_econ: '',
    seat: '',
    duration: ''
  })

  let confort = ref({
    name: '',
    price_conf: '',
    bed: '',
    duration: ''
  })

  async function renderCities() {
    cities.value = await getCities()
  }

  async function submit() {
    const travels = await getTravels(destiny.value)

    economic.value = travels.economic
    confort.value = travels.confort
  }
  
  renderCities()
  
</script>

<template>
  <section class="grid mx-auto grid-cols-12 h-screen">
    <div class="h-full col-span-3 bg-[#2a3040]"></div>

    <div class="flex flex-col h-full col-span-9 bg-[#f8f8f8]">
      <div class="h-[80px] shadow-xl"></div>

      <div class="h-full w-full flex items-center justify-center px-10">
        <div class="w-full">
          <div class="rounded-t-md h-[65px] w-full px-8 py-2 bg-[#2a3040] flex items-center">
            Calculadora de Viagem
          </div>
          <div class="rounded-b-md bg-white p-5 flex gap-3">
            <div class="bg-[#f3f3f3] px-8 min-h-[500px] xl:w-[400px] gap-5 flex flex-col justify-center">
              <h1>Calcule o Valor da Viagem</h1>
              <label for="destiny">Destino</label>
              <select name="destiny" id="destiny" v-model="destiny">
                <option v-for="(city, index) in cities" :key="index" :value="city">{{ city }}</option>
              </select>

              <label for="date">Data</label>
              <input type="date" name="date" id="date" placeholder="Selecione uma data">

              <button class="bg-[#04a8b2]" @click="submit">Buscar</button>
            </div>
            <div class="w-full xl:w-[700px] flex flex-col items-center justify-center">
              <h1>Nenhum dado selecionado</h1>
              <div>
                <div>
                  {{ economic }}
                </div>
                <div>
                  {{ confort }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

