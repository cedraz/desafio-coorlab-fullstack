<script setup>

const props = defineProps({
  wrongFormData: Boolean,
  closeForm: Function
})

import { PhWarning } from "@phosphor-icons/vue";

</script>

<template>
    <div v-if="props.wrongFormData === true" id="default-modal" tabindex="-1" aria-hidden="true" class="bg-opacity-60 bg-black flex items-center justify-center fixed inset-0">
        <div class="relative w-full max-w-[500px] max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow">
                <!-- Modal header -->
                <div class="flex flex-col gap-5 items-center py-14 justify-between border-b rounded-lg">
                    <ph-warning :size="32" color="#02a9b2" />
                    <h3 class="text-xl font-semibold">
                        Insira os valores para realizar a cotação
                    </h3>
                    <button @click="props.closeForm" type="button" class="rounded-lg text-white py-1 px-8 bg-[#02a9b2]" data-modal-hide="default-modal">
                        Fechar
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
