import { api } from './config/axios'

export async function getCities() {
    try {
        const response = await api.get('/cities')
        return response.data
    } catch (error) {
        console.error(error)
    }
}