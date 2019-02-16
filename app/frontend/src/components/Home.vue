<template>
    <div>
        <p>Organização financeira</p>
        <p>Random number from backend: {{ randomNumber }}</p>
        <button @click="getRandom" class="btn">New random number</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(res => {
          this.randomNumber = res.data.randomNumber
        }).catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
