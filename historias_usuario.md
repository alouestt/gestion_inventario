# Historias de Usuario del Proyecto “Sistema de Gestión de Inventarios”

---

## 1. Registrar producto

**Historia de usuario:**  
Como usuario del sistema, quiero registrar un producto ingresando su nombre, para poder almacenarlo en la lista de inventario.

**Criterios de aceptación:**
- El sistema debe permitir ingresar un nombre de producto desde la consola.
- Si el nombre está vacío o contiene solo espacios, debe mostrar el mensaje: `"El nombre no puede estar vacío."`
- Si el producto ya existe (sin distinguir mayúsculas/minúsculas), debe mostrar: `"El producto ya está registrado."`
- Si el producto es válido y no está repetido, debe agregarse a la lista y mostrarse: `"Producto registrado."`
- El producto debe aparecer en el listado después del registro.
- El nombre debe almacenarse con la primera letra en mayúscula (`capitalize()`).

---

## 2. Listar productos

**Historia de usuario:**  
Como usuario del sistema, quiero ver un listado de todos los productos registrados, para saber qué productos tengo en inventario.

**Criterios de aceptación:**
- Al seleccionar la opción "Listar productos", debe mostrarse en consola una lista numerada de productos.
- Si no hay productos registrados, debe mostrarse el mensaje: `"No hay productos registrados."`
- La lista debe contener todos los productos almacenados en memoria.

---

## 3. Buscar producto

**Historia de usuario:**  
Como usuario del sistema, quiero buscar productos por nombre parcial o completo, para encontrar rápidamente un producto específico.

**Criterios de aceptación:**
- El sistema debe solicitar el nombre del producto a buscar.
- Debe buscar sin distinguir entre mayúsculas y minúsculas.
- Debe mostrar todos los productos que contengan la cadena ingresada.
- Si no se encuentra ningún producto, debe mostrarse: `"No se encontraron productos."`

---

## 4. Editar producto

**Historia de usuario:**  
Como usuario del sistema, quiero editar el nombre de un producto existente, para poder corregir o actualizar su información.

**Criterios de aceptación:**
- El sistema debe solicitar el nombre del producto a editar.
- Debe permitir cancelar la edición escribiendo `"salir"`, mostrando: `"Edición cancelada."`
- Si el producto no existe, debe mostrarse: `"Producto no encontrado. Intente de nuevo."`
- Si existe, debe solicitar un nuevo nombre.
- Si el nuevo nombre está vacío, debe mostrar: `"El nuevo nombre no puede estar vacío."` y volver a solicitarlo.
- Una vez actualizado, debe mostrarse: `"Producto actualizado."` y reflejarse en el listado.

---

## 5. Eliminar producto

**Historia de usuario:**  
Como usuario del sistema, quiero eliminar un producto por su nombre, para mantener actualizado el inventario eliminando productos innecesarios.

**Criterios de aceptación:**
- El sistema debe solicitar el nombre del producto a eliminar.
- Debe permitir cancelar la eliminación escribiendo `"salir"`, mostrando: `"Eliminación cancelada."`
- Si el producto existe (sin distinguir mayúsculas/minúsculas), debe eliminarse y mostrarse: `"Producto eliminado."`
- Si no se encuentra, debe mostrarse: `"Producto no encontrado. Intente de nuevo."`
- El producto eliminado no debe aparecer más en la lista.

---

## 6. Prevenir duplicados

**Historia de usuario:**  
Como usuario del sistema, quiero evitar registrar productos con el mismo nombre, para no tener productos duplicados en el inventario.

**Criterios de aceptación:**
- Antes de registrar, el sistema debe verificar si el producto ya existe (sin distinguir mayúsculas/minúsculas).
- Si existe, debe mostrar: `"El producto ya está registrado."`
- El producto no debe agregarse nuevamente.

---

## 7. Validar entradas vacías

**Historia de usuario:**  
Como usuario del sistema, quiero evitar registrar o modificar productos con nombres vacíos, para asegurar que cada producto tenga un nombre válido.

**Criterios de aceptación:**
- Si el usuario ingresa un nombre vacío (o solo espacios) al registrar o editar, debe mostrarse: `"El nombre no puede estar vacío."` o `"El nuevo nombre no puede estar vacío."`
- El sistema no debe almacenar productos con nombres vacíos.

---

## 8. Menú de navegación

**Historia de usuario:**  
Como usuario del sistema, quiero un menú interactivo con opciones numeradas, para poder acceder fácilmente a cada funcionalidad.

**Criterios de aceptación:**
- Al iniciar el programa, debe mostrarse un menú con las opciones numeradas del 1 al 6.
- El menú debe repetirse tras cada acción, hasta que se elija `"Salir"`.
- Si el usuario ingresa una opción inválida, debe mostrarse el mensaje: `"Opción inválida."`
- Al seleccionar `"Salir"`, debe mostrarse el mensaje: `"Ha salido del sistema."`