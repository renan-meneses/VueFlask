<template>
  <!-- eslint-disable-next-line vue/max-attributes-per-line -->
  <div class="container" >
    <div class="row">
      <div class="col-sm-10">
        <h1>Pessoas</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <!-- eslint-disable-next-line vue/max-attributes-per-line -->
        <div>
        <button type="button" class="btn btn-success" v-b-modal.Pessoas-modal>Add Pessoas</button>
        </div>
        <br><br>
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Nome</th>
              <th scope="col">Admissão</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(pessoas, index) in pessoas" :key="index">
              <td>{{ pessoas.nome | formatName }}</td>
              <td>{{ pessoas.data_admissao | formatDate}}</td>
              <td>
                <div class="btn-group" role="group">
                 <!-- <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.Pessoas-update-modal
                          @click="editPessoa(pessoas)">
                      Atualizar
                  </button>-->
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeletePessoa(pessoas)">
                      Excluir
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addPessoasModal"
            id="Pessoas-modal"
            title="Add a new Pessoas"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-nome-edit-group"
                    label="Nome:"
                    label-for="form-nome-edit-input">
          <b-form-input id="form-nome-edit-input"
                        type="text"
                        v-model="addPessoasForm.nome"
                        required
                        >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-rg-edit-group"
                      label="Rg:"
                      label-for="form-rg-edit-input">
            <b-form-input id="form-rg-edit-input"
                          type="text"
                          v-model="addPessoasForm.rg"
                          required
                          >
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-cpf-edit-group"
                      label="CPF:"
                      label-for="form-cpf-edit-input">
            <b-form-input id="form-cpf-edit-input"
                          type="text"
                          v-model="addPessoasForm.cpf"
                          required
                          >
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-dat_nascimento-edit-group"
                      :aria-describedby="ariaDescribedby"
                      label="Data de Nascimento:"
                      label-for="form-dat_nascimento-edit-input"
                      class="pt-2"
                      calendar-width="100%"
                      menu-class="w-100"
                      >

            <b-form-datepicker id="form-dat_nascimento-edit-input"
                          :date-format-options="{year:'numeric', month:'numeric',day:'numeric'}"
                          v-model="addPessoasForm.data_nascimento"
                          required
                          calendar-width="100%"
                          menu-class="w-100"
                          >
            </b-form-datepicker>
          </b-form-group>
          <br>
          <b-form-group id="form-dat_nascimento-edit-group"
                      label="Admissão:"
                      label-for="form-dat_nascimento-edit-input">
            <b-form-datepicker id="form-dat_nascimento-edit-input"
                          :date-format-options="{year:'numeric', month:'numeric',day:'numeric'}"
                          v-model="addPessoasForm.data_admissao"
                          required
                          placeholder="teste"
                          calendar-width="100%"
                          menu-class="w-100"
                          >
            </b-form-datepicker>
          </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editPessoasModal"
            id="Pessoas-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-nome-edit-group"
                    label="Nome:"
                    label-for="form-nome-edit-input">
          <b-form-input id="form-nome-edit-input"
                        type="text"
                        v-model="editForm.nome"
                        required
                        >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-rg-edit-group"
                      label="Rg:"
                      label-for="form-rg-edit-input">
            <b-form-input id="form-rg-edit-input"
                          type="text"
                          v-model="editForm.rg"
                          required
                          >
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-cpf-edit-group"
                      label="CPF:"
                      label-for="form-cpf-edit-input">
            <b-form-input id="form-cpf-edit-input"
                          type="text"
                          v-model="editForm.cpf"
                          required
                          >
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-dat_nascimento-edit-group"
                      label="Data de Nascimento:"
                      class="mb-0"
                     >
            <b-form-datepicker id="form-dat_nascimento-edit-input"
                          :date-format-options="{year:'numeric', month:'numeric',day:'numeric'}"
                          :date-disabled-fn="dateDisabled"
                          v-model="editForm.data_nascimento"
                          required
                          size="sm"
                          >
            </b-form-datepicker>
          </b-form-group>
          <b-form-group id="form-dat_nascimento-edit-group"
                      label="Admissão:"
                      label-for="form-dat_nascimento-edit-input">
            <b-form-datepicker id="form-dat_nascimento-edit-input"
                          :date-format-options="{year:'numeric', month:'numeric',day:'numeric'}"
                          v-model="editForm.data_admissao"
                          required
                          >
            </b-form-datepicker>
          </b-form-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import moment from 'moment';
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      pessoas: [],
      addPessoasForm: {
        nome: '',
        rg: '',
        cpf: '',
        data_nascimento: '',
        data_admissao: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        nome: '',
        rg: '',
        cpf: '',
        data_nascimento: '',
        data_admissao: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  filters: {
    formatDate(value) {
      return moment(String(value)).format('DD/MM/YYYY');
    },
    formatName(value) {
      return String(value).split(' ')[0];
    },
  },
  methods: {
    getPessoas() {
      const path = 'http://localhost:5000/pessoas';
      axios
        .get(path)
        .then((res) => {
          this.pessoas = res.data.pessoas;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addPessoas(payload) {
      const path = 'http://localhost:5000/pessoas';
      axios
        .post(path, payload)
        .then(() => {
          this.getPessoas();
          this.message = 'Pessoa Adicionada!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getPessoas();
        });
    },
    initForm() {
      this.addPessoasForm.nome = '';
      this.addPessoasForm.rg = '';
      this.addPessoasForm.cpf = '';
      this.addPessoasForm.data_nascimento = '';
      this.addPessoasForm.data_admissao = '';

      this.editForm.id_pessoa = '';
      this.editForm.nome = '';
      this.editForm.rg = '';
      this.editForm.cpf = '';
      this.editForm.data_nascimento = '';
      this.editForm.data_admissao = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addPessoasModal.hide();
      const payload = {
        nome: this.addPessoasForm.nome,
        rg: this.addPessoasForm.rg,
        cpf: this.addPessoasForm.cpf,
        data_nascimento: this.addPessoasForm.data_nascimento,
        data_admissao: this.addPessoasForm.data_admissao,
      };
      this.addPessoas(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addPessoasModal.hide();
      this.initForm();
    },
    editPessoa(pessoa) {
      this.editForm = pessoa;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editpessoaModal.hide();

      const payload = {
        nome: this.editForm.nome,
        rg: this.editForm.rg,
        cpf: this.editForm.cpf,
        data_nascimento: this.editForm.data_nascimento,
        data_admissao: this.editForm.data_admissao,
      };
      this.updatePessoa(payload, this.editForm.id_pessoa);
    },
    updatePessoa(payload, pessoaID) {
      const path = `http://localhost:5000/pessoas/${pessoaID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getPessoas();
          this.message = 'Pessoa Editada!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPessoas();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editpessoaModal.hide();
      this.initForm();
      this.getPessoas(); // why?
    },
    removePessoa(pessoaID) {
      const path = `http://localhost:5000/pessoas/${pessoaID}`;
      axios
        .delete(path)
        .then(() => {
          this.getPessoas();
          this.message = 'Pessoa removida!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPessoas();
        });
    },
    onDeletePessoa(pessoa) {
      this.removePessoa(pessoa.id_pessoa);
    },
  },
  created() {
    this.getPessoas();
  },
};
</script>
