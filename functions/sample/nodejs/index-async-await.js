/**
 * Get all dealerships
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
      const authenticator = new IamAuthenticator({ apikey: "jIgFW3QzX8e_k8aAWhYA4SaeDfXQ62Jy0szogP5-eVJa" })
      const cloudant = CloudantV1.newInstance({
          authenticator: authenticator
      });
      cloudant.setServiceUrl("https://apikey-v2-rg5tzn3w5twkdi5w3oiiwrc8i3qlbhhmy8miw6ptjtx:11749eab45d913ef5e98f4276a578e76@148477bd-c1eb-4521-a003-97beae46f41d-bluemix.cloudantnosqldb.appdomain.cloud");
      try {
        let dbList = await cloudant.getAllDbs();
        return { "dbs": dbList.result };
      } catch (error) {
          return { error: error.description };
      }
}

