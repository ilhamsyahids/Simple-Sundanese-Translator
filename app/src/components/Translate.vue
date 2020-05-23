<template>
  <div class="hello">
    <b-alert v-model="showAlert" variant="danger" dismissible>
      Fill the form!
    </b-alert>
    <b-alert v-model="showAlertVocab" variant="warning" dismissible>
      Not in the vocabulary
    </b-alert>
    <h1>{{ msg }}</h1>
    <div class="mb-4">
      <p>
        <b>Options Languages:</b>
      </p>
      <div>
        <b-form-select
          v-model="uploadSelected"
          class="mb-4"
          style="max-width:20rem;"
          :options="uploadOptions"
        />
      </div>
      <b-form-file
        :state="Boolean(upload.dicts) || defaultVocab"
        :disabled="defaultVocab"
        style="max-width:35rem;"
        size="lg"
        :placeholder="'File Vocab ' + (uploadSelected == 'sunda' ? 'Sunda - Indonesia' : 'Indonesia - Sunda')"
        @change="filesChange($event.target.name, $event.target.files)"
        no-drop
        accept="text/*"
      >
      </b-form-file>
      <p>
        <span>Use default vocab </span>
        <b-checkbox
          v-model="defaultVocab"
          style="display: inline-block"
        />
      </p>
    </div>
    <div class="mb-4">
      <p>
        <b>Text :</b>
      </p>
      <b-form-textarea
        :state="Boolean(words)"
        style="max-width: 40rem;margin-left: auto;margin-right:auto"
        type="text"
        name="words"
        id="words"
        v-model="words"
        placeholder="Enter something..."
        rows="3"
        max-rows="6"
      />
    </div>
    <div>
      <p>
        <b>Algorithm:</b>
      </p>
      <b-form-select
        v-model="algorithm"
        :state="Boolean(algorithm)"
        class="mb-4"
        style="max-width:20rem;"
        :options="algorithmOptions"
      />
    </div>

    <h3>
      <b-button @click="onUploadHandler()" variant="success">
        Upload
      </b-button>
    </h3>

    <template v-if="result">
    <h3>Translation: </h3>
      <b-card
        border-variant="primary"
        header-bg-variant="dark"
        header-text-variant="white"
        style="max-width: 40rem;margin-left: auto;margin-right:auto"
        class="mb-4"
        body-class="text-center"
      >
        <b-card-text v-html="result" />
      </b-card>
    </template>
    <footer class="mt-4 mb-4">
      Made with <BIconHeartFill /> by ilhamsyahids
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import { BIconHeartFill } from 'bootstrap-vue'

export default {
  name: "Uploader",
  props: {
    msg: String
  },
  components: {
    BIconHeartFill
  },
  data() {
    return {
      uploadOptions: [
        { value: 'sunda', text: 'Sunda-Indonesia' },
        { value: 'indo', text: 'Indonesia-Sunda' }
      ],
      algorithmOptions: [
        { value: 'Regex', text: 'Regex' },
        { value: 'Boyer', text: 'Boyer-Moore' },
        { value: 'KMP', text: 'Knuth Morris Pratt' }
      ],
      uploadSelected: 'sunda',
      result: null,
      upload: {
        dicts: null
      },
      showAlert: false,
      showAlertVocab: false,
      words: null,
      defaultVocab: false,
      renderKeyword: null,
      algorithm: "Regex"
    };
  },
  methods: {
    filesChange(name, files) {
      if (!files.length) return;
      const dicts = {}
      for (let i = 0; i < files.length; i++) {
        this.readFileContent(files[i]).then(res => {
          const sentences = res.split('\n');
          sentences.forEach(el => {
            const dict = el.split(' = ').filter(r => r)
            dicts[dict[0]] = dict[1];
          });
        })
      }
      this.upload.dicts = dicts;
    },
    readFileContent(file) {
      const reader = new FileReader();
      return new Promise((resolve, reject) => {
        reader.onload = event => resolve(event.target.result);
        reader.onerror = error => reject(error);
        reader.readAsText(file);
      });
    },
    onUploadHandler() {
      const {
        words,
        algorithm,
        uploadSelected,
        upload,
        defaultVocab,
      } = this;
      if (!words || !algorithm || !uploadSelected || !(upload.dicts || defaultVocab)) {
        this.showAlert = true
        return
      } else {
        this.showAlert = false
      }
      this.result = null
      this.showAlertVocab = false
      upload.algorithm = algorithm
      upload.words = words.split(' ').filter(item => item)
      upload.selected = uploadSelected
      upload.default = defaultVocab
      axios.post(process.env.VUE_APP_API_URL || "http://localhost:5000", this.upload)
        .then(res => {
          console.log(this.upload)
          console.log(res.data.data)
          if (res.data.data) {
            this.result = res.data.data
          } else {
            this.showAlertVocab = true
          }
        }).catch((err) => {
          console.log(err)
        })
    }
  }
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #4289b9;
}
</style>
