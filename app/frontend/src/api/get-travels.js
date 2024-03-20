import { api } from './config/axios'

export async function getTravels(city) {
    try {
        const response = await api.post('/travel', {
            city: city
        })

        return response.data
    } catch (error) {
        console.error(error)
    }
}