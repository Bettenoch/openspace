import axios from 'axios';
import createAuthRefreshInterceptor from 'axios-auth-refresh';


const axiosService = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {'Content-Type': 'application/json'},
});

axiosService.interceptors.request.use(async (config) => {
    /**
     * Retrieving the access and refresh tokens from the local storage
     */
    const  {access} = JSON.parse(localStorage.getItem("auth"));
    config.headers.Authorization = `Bearer ${access}`;
    return config;
  });

  axiosService.interceptors.response.use(
    (res) => Promise.resolve(res),
    (err) => Promise.reject(err)
  );

  const refreshAuthLogic = async (failedRequest) => {
    const {refresh} = JSON.parse(localStorage.getItem('auth'));
    return axios
      .post(
        "/refresh/token",
        {
          refresh: getRefreshToken(),
        },
        {
          baseURL: "http://localhost:8000/api",
        }
      )
      .then((resp) => {
        const { access } = resp.data;
        failedRequest.response.config.headers["Authorization"] =
          "Bearer " + access;
        localStorage.setItem(
          "auth",
          JSON.stringify({ access, refresh: getRefreshToken(), user: getUser() })
        );
      })
      .catch(() => {
        localStorage.removeItem("auth");
      });
  };